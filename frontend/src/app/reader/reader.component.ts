import { Component } from '@angular/core';
import { ReaderService } from './reader.service';
import { ActivatedRoute } from '@angular/router';

import { Book, WordDef } from './interfaces';

@Component({
  selector: 'reader',
  templateUrl: './reader.component.html',
  styleUrls: ['./reader.component.scss'],
})
export class ReaderComponent {
  book: Book | null = null;
  currentWord: string | null = null;
  currentDefinition: WordDef[] = [];

  constructor(private route: ActivatedRoute, private service: ReaderService) {}

  ngOnInit(): void {
    const filename = this.route.snapshot.paramMap.get('filename');
    this.book = filename ? this.service.getBook(filename) : null;
  }

  handleWordSelected(word: string) {
    const defintion = this.service.getWordDefinition(word);
    this.currentDefinition = defintion;
    this.currentWord = word;
  }
}
