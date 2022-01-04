import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReaderComponent } from './reader.component';
import { BookContentComponent } from './book-content/book-content.component';

@NgModule({
  declarations: [ReaderComponent, BookContentComponent],
  imports: [CommonModule],
})
export class ReaderModule {}
