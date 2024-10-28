import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKLOCATION_MODULE_DECLARATIONS, WalkLocationRoutingModule} from  './WalkLocation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkLocationRoutingModule
  ],
  declarations: WALKLOCATION_MODULE_DECLARATIONS,
  exports: WALKLOCATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkLocationModule { }