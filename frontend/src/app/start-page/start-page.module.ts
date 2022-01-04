import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';

import { StartPageComponent } from './start-page.component';
import { BookCardComponent } from './book-card/book-card.component';

@NgModule({
  declarations: [StartPageComponent, BookCardComponent],
  imports: [
    CommonModule,
    RouterModule,
    MatCardModule,
    MatProgressBarModule,
    MatButtonModule,
  ],
})
export class StartPageModule {}
