export interface Book {
  title: string;
  author: string;
  content: string;
}

export enum Aspects {
  IMPERFECTIVE,
  PERFECTIVE,
}

export enum Pos {
  VERB,
  NOUN,
  PREPOSITION,
  ADJECTIVE,
  ADVERB,
  NUMERAL,
  PRONOUN,
  CONJUNCTION,
}

export enum Gender {
  MASCULINE,
  FEMININE,
  NEUTER,
}

export interface Example {
  sentence: string;
  translation: string;
}

export interface Translation {
  translation: string;
  examples: Example[];
}

export interface WordDef {
  lemma: string;
  pos: Pos;
  aspect?: Aspects;
  gender?: Gender;
  translations: Translation[];
}
