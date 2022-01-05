import { forwardRef, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
  useClass: forwardRef(() => AppServiceMocked),
})
export abstract class AppService {
  abstract uploadBook(file: File): void;
}

@Injectable({
  providedIn: 'root',
})
export class AppServiceMocked extends AppService {
  uploadBook(file: File): void {
    alert(`
    File uploaded
    File name: ${file.name}
    File type: ${file.type}
    `);
  }
}
