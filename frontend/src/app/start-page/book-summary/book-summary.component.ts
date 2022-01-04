import { Component, Input, OnInit } from '@angular/core';
import { Book, WordStats } from '../interfaces';
import { ChartOptions, ChartData } from 'chart.js';

@Component({
  selector: 'app-book-summary',
  templateUrl: './book-summary.component.html',
  styleUrls: ['./book-summary.component.scss'],
})
export class BookSummaryComponent implements OnInit {
  @Input() book: Book | undefined = undefined;
  @Input() words: WordStats = [];

  data: ChartData = { datasets: [] };
  options: ChartOptions = {};

  constructor() {
    this.makeChartData();
    this.makeChartOptions();
  }

  ngOnInit(): void {}

  ngOnChanges(): void {
    this.makeChartData();
  }

  private makeChartData() {
    this.data = {
      datasets: [
        {
          type: 'bar',
          //@ts-expect-error
          data: this.words,
        },
      ],
    };
  }

  private makeChartOptions() {
    this.options = {};

    this.options = {
      indexAxis: 'y',
    };

    this.options.plugins = this.pluginsOptions();
    this.options.scales = {
      yAxis: this.yAxisOptions(),
      xAxis: this.xAxisOptions(),
    };
    this.options.parsing = this.parsingOptions();
    this.options.elements = {
      bar: this.barOptions(),
    };
  }

  private pluginsOptions() {
    const plugins = {
      tooltip: {
        enabled: false,
      },
      legend: {
        display: false,
      },
    };
    return plugins;
  }

  private yAxisOptions() {
    const yAxis = {
      reverse: false,
    };
    return yAxis;
  }

  private xAxisOptions() {
    const xAxis = {
      ticks: {
        callback: BookSummaryComponent.yLabelFormatter,
      },
    };
    return xAxis;
  }

  private parsingOptions() {
    const parsing = {
      xAxisKey: 'freq',
      yAxisKey: 'word',
    };
    return parsing;
  }

  private barOptions() {
    const bar = {
      borderWidth: 2,
    };
    return bar;
  }

  private static yLabelFormatter(value: number | string): string {
    const valueNum = value as number;
    const percentage = (valueNum * 100).toFixed(0) + '%';
    return percentage;
  }
}
