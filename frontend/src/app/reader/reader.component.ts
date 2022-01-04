import { Component } from '@angular/core';
import { ReaderService } from './reader.service';
import { ActivatedRoute } from '@angular/router';

import { Book } from './interfaces';

@Component({
  selector: 'reader',
  templateUrl: './reader.component.html',
  styleUrls: ['./reader.component.scss'],
})
export class ReaderComponent {
  book: Book | null = null;

  constructor(private route: ActivatedRoute, private service: ReaderService) {}

  ngOnInit(): void {
    const filename = this.route.snapshot.paramMap.get('filename');
    this.book = filename ? this.service.getBook(filename) : null;
  }
}
