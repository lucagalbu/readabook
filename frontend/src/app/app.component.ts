import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  onViewActivate() {
    document.querySelector('#main-scrollable-container')!.scrollTo(0, 0);
  }
}
