import { Component } from '@angular/core';
import { StartPageService } from './start-page.service';

@Component({
  selector: 'start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss'],
})
export class StartPageComponent {
  constructor(private service: StartPageService) {}
}
