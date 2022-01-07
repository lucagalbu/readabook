import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AppService } from '../app.service';

@Component({
  selector: 'app-new-book',
  templateUrl: './new-book.component.html',
  styleUrls: ['./new-book.component.scss'],
})
export class NewBookComponent implements OnInit {
  file: File | null = null;
  infoForm = new FormGroup({
    title: new FormControl(''),
    author: new FormControl(''),
  });

  @ViewChild('fileInput') fileInputLement:
    | ElementRef<HTMLInputElement>
    | undefined = undefined;

  constructor(private service: AppService) {}

  handleFileInputChange(event: Event) {}

  handleFormSubmit() {
    this.fileInputLement?.nativeElement.click();
  }

  ngOnInit(): void {}
}
