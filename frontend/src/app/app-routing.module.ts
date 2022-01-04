import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { StartPageComponent } from './start-page/start-page.component';
import { ReaderComponent } from './reader/reader.component';

const appRoutes: Routes = [
  { path: 'start-page', component: StartPageComponent },
  { path: 'reader/:filename', component: ReaderComponent },
  { path: '', redirectTo: '/start-page', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
