import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export abstract class AppService {
  abstract uploadBook(file: File): void;
}
