import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'extractSubtitle',
})
export class ExtractSubtitlePipe implements PipeTransform {
  transform(value: any) {
    return value;
  }
}
