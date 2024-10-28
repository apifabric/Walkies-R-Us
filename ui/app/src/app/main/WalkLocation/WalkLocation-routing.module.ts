import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkLocationHomeComponent } from './home/WalkLocation-home.component';
import { WalkLocationNewComponent } from './new/WalkLocation-new.component';
import { WalkLocationDetailComponent } from './detail/WalkLocation-detail.component';

const routes: Routes = [
  {path: '', component: WalkLocationHomeComponent},
  { path: 'new', component: WalkLocationNewComponent },
  { path: ':id', component: WalkLocationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkLocation-detail-permissions'
      }
    }
  }
];

export const WALKLOCATION_MODULE_DECLARATIONS = [
    WalkLocationHomeComponent,
    WalkLocationNewComponent,
    WalkLocationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkLocationRoutingModule { }