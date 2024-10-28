import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkLocation-new',
  templateUrl: './WalkLocation-new.component.html',
  styleUrls: ['./WalkLocation-new.component.scss']
})
export class WalkLocationNewComponent {
  @ViewChild("WalkLocationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}