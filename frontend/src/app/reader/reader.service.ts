import { Injectable } from '@angular/core';
import { Book, WordDef } from './interfaces';

@Injectable({
  providedIn: 'root',
})
export abstract class ReaderService {
  abstract getBook(filename: string): Book | null;
  abstract getWordDefinition(word: string): WordDef[];
}
