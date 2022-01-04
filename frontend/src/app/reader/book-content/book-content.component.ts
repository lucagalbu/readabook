import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Book } from '../interfaces';

@Component({
  selector: 'book-content',
  templateUrl: './book-content.component.html',
  styleUrls: ['./book-content.component.scss'],
})
export class BookContentComponent implements OnInit {
  @Input() book: Book;
  @Output() wordSelected = new EventEmitter<string>();

  constructor() {
    this.book = { title: '', author: '', content: '' };
  }

  ngOnInit(): void {}

  onClick(e: MouseEvent) {
    const selection = window.getSelection()?.toString();
    if (!selection) return;

    const word = BookContentComponent.getWordFromSelection(selection);
    if (!word) return;

    this.wordSelected.emit(word);
  }

  private static getWordFromSelection(selection: string): string | null {
    let words: string[] | null;
    if (selection !== '') {
      words = selection.trim().split(' ');
    } else {
      words = null;
    }

    if (words && words.length === 1) {
      return words[0];
    } else {
      return null;
    }
  }
}
