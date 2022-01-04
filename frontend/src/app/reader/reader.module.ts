import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatCardModule } from '@angular/material/card';

import { ReaderComponent } from './reader.component';
import { BookContentComponent } from './book-content/book-content.component';
import { DictionaryComponent } from './dictionary/dictionary.component';

import { ExtractSubtitlePipe } from './extract-subtitle.pipe';

@NgModule({
  declarations: [
    ReaderComponent,
    BookContentComponent,
    DictionaryComponent,
    ExtractSubtitlePipe,
  ],
  imports: [CommonModule, MatCardModule],
})
export class ReaderModule {}
