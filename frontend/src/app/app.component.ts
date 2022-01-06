import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

import { AppService } from './app.service';
import { NewBookComponent } from './new-book/new-book.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private service: AppService, public dialog: MatDialog) {}

  onViewActivate() {
    document.querySelector('#main-scrollable-container')!.scrollTo(0, 0);
  }

  onNewBookClick() {
    this.dialog.open(NewBookComponent);
  }

  onBookUpload(event: Event) {
    const target = event.target as HTMLInputElement;
    target.files && target.files[0] && this.service.uploadBook(target.files[0]);
  }
}
