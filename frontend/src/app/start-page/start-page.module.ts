import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';

import { StartPageComponent } from './start-page.component';
import { BookCardComponent } from './book-card/book-card.component';
import { BookSummaryComponent } from './book-summary/book-summary.component';

@NgModule({
  declarations: [StartPageComponent, BookCardComponent, BookSummaryComponent],
  imports: [
    CommonModule,
    RouterModule,
    MatCardModule,
    MatProgressBarModule,
    MatButtonModule,
    MatDividerModule,
  ],
})
export class StartPageModule {}
