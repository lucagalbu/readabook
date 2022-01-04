import { forwardRef, Injectable } from '@angular/core';
import { Book, WordStats } from './interfaces';

@Injectable({
  providedIn: 'root',
  useClass: forwardRef(() => StartPageServiceMocked),
})
export abstract class StartPageService {
  abstract getBooks(): Book[];
  abstract getWordStats(filename: string, maxWords?: number): WordStats;
}

@Injectable({
  providedIn: 'root',
})
export class StartPageServiceMocked extends StartPageService {
  getBooks(): Book[] {
    return [
      {
        title: 'Про слона',
        author: 'Борис Житков',
        filename: 'про_слона.txt',
        dateAdded: new Date('1 December 2021'),
        uniqueWords: 1024,
        wordsLearned: 500,
        fractionLearned: 0.8,
      },
      {
        title: 'Рассказы',
        author: 'Димитрий Мамин-Сибиряк',
        filename: 'рассказы.txt',
        dateAdded: new Date('15 December 2021'),
        uniqueWords: 2048,
        wordsLearned: 458,
        fractionLearned: 0.6,
      },
      {
        title: 'Иностранка',
        author: 'Сергей Довлатов',
        filename: 'иностранка.txt',
        dateAdded: new Date('27 November 2021'),
        uniqueWords: 947,
        wordsLearned: 128,
        fractionLearned: 0.56,
      },
    ];
  }

  getWordStats(filename: string, maxWords?: number): WordStats {
    switch (filename) {
      case 'про_слона.txt':
        return this.проСлонаWords().slice(0, maxWords);
      case 'рассказы.txt':
        return this.рассказыWords().slice(0, maxWords);
      case 'иностранка.txt':
        return this.иностранкаWords().slice(0, maxWords);
      default:
        return [];
    }
  }

  private проСлонаWords(): WordStats {
    const words = [
      { word: 'history', freq: 0.08 },
      { word: 'past', freq: 0.06 },
      { word: 'from', freq: 0.03 },
      { word: 'historical', freq: 0.027 },
      { word: 'events', freq: 0.024 },
      { word: 'historians', freq: 0.019 },
      { word: 'study', freq: 0.014 },
      { word: 'narrative', freq: 0.013 },
      { word: 'word', freq: 0.011 },
      { word: 'written', freq: 0.01 },
    ];
    return words;
  }

  private рассказыWords(): WordStats {
    const words = [
      { word: 'legend', freq: 0.053 },
      { word: 'folktale', freq: 0.045 },
      { word: 'narrative', freq: 0.035 },
      { word: 'word', freq: 0.031 },
      { word: 'legendary', freq: 0.025 },
      { word: 'question', freq: 0.021 },
      { word: 'content', freq: 0.017 },
      { word: 'early', freq: 0.011 },
      { word: 'english', freq: 0.009 },
      { word: 'rumour', freq: 0.008 },
    ];
    return words;
  }

  private иностранкаWords(): WordStats {
    const words = [
      { word: 'experience', freq: 0.068 },
      { word: 'moral', freq: 0.04 },
      { word: 'knowledge', freq: 0.026 },
      { word: 'transcendental', freq: 0.024 },
      { word: 'priori', freq: 0.023 },
      { word: 'itself', freq: 0.022 },
      { word: 'world', freq: 0.021 },
      { word: 'philosophy', freq: 0.019 },
      { word: 'category', freq: 0.012 },
      { word: 'mind', freq: 0.011 },
    ];
    return words;
  }
}
