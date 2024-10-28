import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DogWalkerHomeComponent } from './home/DogWalker-home.component';
import { DogWalkerNewComponent } from './new/DogWalker-new.component';
import { DogWalkerDetailComponent } from './detail/DogWalker-detail.component';

const routes: Routes = [
  {path: '', component: DogWalkerHomeComponent},
  { path: 'new', component: DogWalkerNewComponent },
  { path: ':id', component: DogWalkerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DogWalker-detail-permissions'
      }
    }
  },{
    path: ':dog_walker_id/Walk', loadChildren: () => import('../Walk/Walk.module').then(m => m.WalkModule),
    data: {
        oPermission: {
            permissionId: 'Walk-detail-permissions'
        }
    }
}
];

export const DOGWALKER_MODULE_DECLARATIONS = [
    DogWalkerHomeComponent,
    DogWalkerNewComponent,
    DogWalkerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DogWalkerRoutingModule { }