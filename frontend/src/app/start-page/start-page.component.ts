import { Component } from '@angular/core';
import { StartPageService } from './start-page.service';
import { Book, WordStats } from './interfaces';

@Component({
  selector: 'start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss'],
})
export class StartPageComponent {
  books: Book[] = [];
  currentBook: Book | undefined;
  words: WordStats = [];

  constructor(private service: StartPageService) {}

  ngOnInit(): void {
    this.books = this.service.getBooks();
    this.selectBook(this.books[0]);
  }

  bookCardClicked(book: Book): void {
    if (book !== this.currentBook) this.selectBook(book);
  }

  private selectBook(book: Book): void {
    this.currentBook = book;
    this.words = this.service.getWordStats(book.filename, 10);
  }
}
