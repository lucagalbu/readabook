import { Component, OnInit, Input } from '@angular/core';
import { Book } from '../interfaces';

@Component({
  selector: 'book-content',
  templateUrl: './book-content.component.html',
  styleUrls: ['./book-content.component.scss'],
})
export class BookContentComponent implements OnInit {
  @Input() book: Book;

  constructor() {
    this.book = { title: '', author: '', content: '' };
  }

  ngOnInit(): void {}
}
