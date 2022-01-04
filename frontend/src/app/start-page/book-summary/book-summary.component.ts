import { Component, Input, OnInit } from '@angular/core';
import { Book, WordStats } from '../interfaces';

@Component({
  selector: 'app-book-summary',
  templateUrl: './book-summary.component.html',
  styleUrls: ['./book-summary.component.scss'],
})
export class BookSummaryComponent implements OnInit {
  @Input() book: Book | undefined = undefined;
  @Input() words: WordStats = [];

  ngOnInit(): void {}
}
