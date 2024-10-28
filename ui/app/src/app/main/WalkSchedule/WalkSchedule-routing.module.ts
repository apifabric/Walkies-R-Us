import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkScheduleHomeComponent } from './home/WalkSchedule-home.component';
import { WalkScheduleNewComponent } from './new/WalkSchedule-new.component';
import { WalkScheduleDetailComponent } from './detail/WalkSchedule-detail.component';

const routes: Routes = [
  {path: '', component: WalkScheduleHomeComponent},
  { path: 'new', component: WalkScheduleNewComponent },
  { path: ':id', component: WalkScheduleDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkSchedule-detail-permissions'
      }
    }
  }
];

export const WALKSCHEDULE_MODULE_DECLARATIONS = [
    WalkScheduleHomeComponent,
    WalkScheduleNewComponent,
    WalkScheduleDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkScheduleRoutingModule { }