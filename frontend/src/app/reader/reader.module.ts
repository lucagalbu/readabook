import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReaderComponent } from './reader.component';
import { BookContentComponent } from './book-content/book-content.component';
import { DictionaryComponent } from './dictionary/dictionary.component';

@NgModule({
  declarations: [ReaderComponent, BookContentComponent, DictionaryComponent],
  imports: [CommonModule],
})
export class ReaderModule {}
