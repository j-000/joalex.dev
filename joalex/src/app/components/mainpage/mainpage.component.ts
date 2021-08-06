import { Component, OnInit, OnDestroy } from '@angular/core';
import { Card } from 'src/app/model/cards';
import { MAINPAGE_CARDS_DATA } from 'src/db-data';

@Component({
  selector: 'app-mainpage',
  templateUrl: './mainpage.component.html',
  styleUrls: ['./mainpage.component.css'],
})
export class MainpageComponent implements OnInit {
  cards: Card[] = MAINPAGE_CARDS_DATA;
  word: string;

  private words: string[] = ['Angular', 'Front-End', 'Full-Stack', 'Python'];
  private next: number = 0;
  private word_changer: any;

  constructor() {}

  ngOnInit(): void {
    this.word = 'Python';
    this.word_changer = setInterval(() => {
      this.word = this.words[this.next];
      this.next++;
      if (this.next >= this.words.length) this.next = 0;
    }, 3000);
  }

  ngOnDestroy() {
    clearInterval(this.word_changer);
  }
}
