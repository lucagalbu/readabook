import { Pipe, PipeTransform } from '@angular/core';
import { WordDef, Pos, Gender, Aspects } from './interfaces';

@Pipe({
  name: 'extractSubtitle',
})
export class ExtractSubtitlePipe implements PipeTransform {
  transform(value: WordDef) {
    const pos = this.posToString(value.pos);
    const gender = this.genderToString(value.gender);
    const aspect = this.aspectToString(value.aspect);

    const terms = [pos, gender, aspect].filter((term) => term);
    return terms.join(', ');
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
