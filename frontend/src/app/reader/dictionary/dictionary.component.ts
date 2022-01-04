import { Component, OnInit, Input } from '@angular/core';
import { WordDef } from '../interfaces';

@Component({
  selector: 'dictionary',
  templateUrl: './dictionary.component.html',
  styleUrls: ['./dictionary.component.scss'],
})
export class DictionaryComponent implements OnInit {
  @Input() word: string | null = null;
  @Input() definitions: WordDef[] = [];

  ngOnInit(): void {}
}
