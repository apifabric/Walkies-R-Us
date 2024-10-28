import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DogWalker-card.component.html',
  styleUrls: ['./DogWalker-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DogWalker-card]': 'true'
  }
})

export class DogWalkerCardComponent {


}