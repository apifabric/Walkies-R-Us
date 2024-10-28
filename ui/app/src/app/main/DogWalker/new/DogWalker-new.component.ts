import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DogWalker-new',
  templateUrl: './DogWalker-new.component.html',
  styleUrls: ['./DogWalker-new.component.scss']
})
export class DogWalkerNewComponent {
  @ViewChild("DogWalkerForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}