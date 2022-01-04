export interface Book {
  title: string;
  author: string;
  filename: string;
  dateAdded: Date;
  uniqueWords: number;
  wordsLearned: number;
  fractionLearned: number;
}

interface SingleWordStats {
  word: string;
  freq: number;
}

export type WordStats = Array<SingleWordStats>;
