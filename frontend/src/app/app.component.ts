import { Component } from '@angular/core';

import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private service: AppService) {}

  onViewActivate() {
    document.querySelector('#main-scrollable-container')!.scrollTo(0, 0);
  }

  onBookUpload(event: Event) {
    const target = event.target as HTMLInputElement;
    target.files && target.files[0] && this.service.uploadBook(target.files[0]);
  }
}
