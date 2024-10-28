import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Client', loadChildren: () => import('./Client/Client.module').then(m => m.ClientModule) },
    
        { path: 'Dog', loadChildren: () => import('./Dog/Dog.module').then(m => m.DogModule) },
    
        { path: 'DogWalker', loadChildren: () => import('./DogWalker/DogWalker.module').then(m => m.DogWalkerModule) },
    
        { path: 'Feedback', loadChildren: () => import('./Feedback/Feedback.module').then(m => m.FeedbackModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Walk', loadChildren: () => import('./Walk/Walk.module').then(m => m.WalkModule) },
    
        { path: 'WalkLocation', loadChildren: () => import('./WalkLocation/WalkLocation.module').then(m => m.WalkLocationModule) },
    
        { path: 'WalkSchedule', loadChildren: () => import('./WalkSchedule/WalkSchedule.module').then(m => m.WalkScheduleModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }