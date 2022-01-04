import { Component } from '@angular/core';
import { ReaderService } from './reader.service';

@Component({
  selector: 'reader',
  templateUrl: './reader.component.html',
  styleUrls: ['./reader.component.scss'],
})
export class ReaderComponent {
  constructor(private service: ReaderService) {}
}
