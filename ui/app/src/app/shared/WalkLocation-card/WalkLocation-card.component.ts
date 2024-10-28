import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkLocation-card.component.html',
  styleUrls: ['./WalkLocation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkLocation-card]': 'true'
  }
})

export class WalkLocationCardComponent {


}