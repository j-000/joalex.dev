import { Card } from './app/model/cards';

export const MAINPAGE_CARDS_DATA: Card[] = [
  {
    htmlText:
      'I am a <span class="wordshine">Computer Science</span> student at Birkbeck, University of London.',
    image: '../../assets/grad.svg',
  },
  {
    htmlText:
      'I develop web applications using <span class="wordshine">Python</span> and <span class="wordshine">JavaScript</span>.',
    image: '../../assets/prog2.svg',
  },
  {
    htmlText:
      'My skills include <span class="wordshine">HTML</span>, <span class="wordshine">CSS</span>, <span class="wordshine">JavaScript</span>, <span class="wordshine">Python</span> and <span class="wordshine">SQL</span>.',
    image: '../../assets/staticweb.svg',
  },
  {
    htmlText: `I am also familiar with development frameworks such as 
      <span class="wordshine">Flask</span>, 
      <span class="wordshine">FastAPI</span>, 
      <span class="wordshine">Django</span>, 
      <span class="wordshine">Angular</span>, 
      <span class="wordshine">VueJs</span>...`,
    image: '../../assets/sourcecode.svg',
  },
  {
    htmlText: `... as well as 
    <span class="wordshine">Git</span>, 
    <span class="wordshine">Docker</span>, 
    <span class="wordshine">ORMs</span>, 
    <span class="wordshine">UI Design</span>, 
    <span class="wordshine">TDD</span> and much more.`,
    image: '../../assets/scrum.svg',
  },
  {
    htmlText: `In my free time, I like to read about 
      <span class="wordshine">finance</span>, 
      <span class="wordshine">business</span> and 
      <span class="wordshine">new tech</span>.`,
    image: '../../assets/read.svg',
  },
  {
    htmlText:
      'There is only so much I can put here. Feel free to download <span class="wordshine">my CV</span>.',
    image: '../../assets/typing.svg',
    cv: true,
  },
  {
    htmlText:
      'Email me at <span class="wordshine">joao00alex@gmail.com</span>.',
    image: '../../assets/contact.svg',
  },
];
