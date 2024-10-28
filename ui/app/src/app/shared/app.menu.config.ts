import { MenuRootItem } from 'ontimize-web-ngx';

import { ClientCardComponent } from './Client-card/Client-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { DogWalkerCardComponent } from './DogWalker-card/DogWalker-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { WalkCardComponent } from './Walk-card/Walk-card.component';

import { WalkLocationCardComponent } from './WalkLocation-card/WalkLocation-card.component';

import { WalkScheduleCardComponent } from './WalkSchedule-card/WalkSchedule-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Client', name: 'CLIENT', icon: 'view_list', route: '/main/Client' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'DogWalker', name: 'DOGWALKER', icon: 'view_list', route: '/main/DogWalker' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Walk', name: 'WALK', icon: 'view_list', route: '/main/Walk' }
    
        ,{ id: 'WalkLocation', name: 'WALKLOCATION', icon: 'view_list', route: '/main/WalkLocation' }
    
        ,{ id: 'WalkSchedule', name: 'WALKSCHEDULE', icon: 'view_list', route: '/main/WalkSchedule' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    ClientCardComponent

    ,DogCardComponent

    ,DogWalkerCardComponent

    ,FeedbackCardComponent

    ,PaymentCardComponent

    ,WalkCardComponent

    ,WalkLocationCardComponent

    ,WalkScheduleCardComponent

];