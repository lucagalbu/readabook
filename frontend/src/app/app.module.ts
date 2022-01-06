import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { NewBookComponent } from './new-book/new-book.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

import { StartPageModule } from './start-page/start-page.module';
import { ReaderModule } from './reader/reader.module';

import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [AppComponent, NewBookComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    MatToolbarModule,
    MatButtonModule,
    MatDialogModule,
    MatInputModule,
    MatMenuModule,
    MatFormFieldModule,
    StartPageModule,
    ReaderModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
