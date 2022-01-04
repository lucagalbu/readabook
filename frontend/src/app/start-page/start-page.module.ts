import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { StartPageComponent } from './start-page.component';
import { BookCardComponent } from './book-card/book-card.component';

@NgModule({
  declarations: [StartPageComponent, BookCardComponent],
  imports: [CommonModule, RouterModule],
})
export class StartPageModule {}
