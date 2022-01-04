import { Pipe, PipeTransform } from '@angular/core';
import { Pos, Gender, Aspects } from './interfaces';

@Pipe({
  name: 'extractSubtitle',
})
export class ExtractSubtitlePipe implements PipeTransform {
  transform(value: any) {
    return value;
  }

  private posToString(value: Pos): string | null {
    switch (value) {
      case Pos.ADJECTIVE:
        return 'Adjective';
      case Pos.ADVERB:
        return 'Adverb';
      case Pos.CONJUNCTION:
        return 'Conjunction';
      case Pos.NOUN:
        return 'Noun';
      case Pos.NUMERAL:
        return 'Numeral';
      case Pos.PREPOSITION:
        return 'Preposition';
      case Pos.PRONOUN:
        return 'Pronoun';
      case Pos.VERB:
        return 'Verb';
      default:
        return null;
    }
  }

  private genderToString(value: Gender | undefined): string | null {
    switch (value) {
      case Gender.FEMININE:
        return 'Feminine';
      case Gender.MASCULINE:
        return 'Masculine';
      case Gender.NEUTER:
        return 'Neuter';
      default:
        return null;
    }
  }

  private aspectToString(value: Aspects | undefined): string | null {
    switch (value) {
      case Aspects.IMPERFECTIVE:
        return 'Imperfective';
      case Aspects.PERFECTIVE:
        return 'Perfective';
      default:
        return null;
    }
  }
}
