import { Injectable } from '@angular/core';
import { Book, WordStats } from './interfaces';

@Injectable({
  providedIn: 'root',
})
export abstract class StartPageService {
  abstract getBooks(): Book[];
  abstract getWordStats(filename: string, maxWords?: number): WordStats;
}
