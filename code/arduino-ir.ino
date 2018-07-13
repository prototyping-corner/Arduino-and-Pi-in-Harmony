/*
 * Demo code for an arduino sensor sender unit
 * Sends back IR temperature and ambient temperature every second
 * over serial
 *
 * Project details at
 * prototypingcorner.io/projects/arduino-and-pi-in-harmony
 *
 * MIT License
 *
 * Copyright (c) 2018 Prototyping Corner
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include "IRTemp.h"

static const byte PIN_DATA   = 4;
static const byte PIN_CLOCK  = 5;
static const byte PIN_AQUIRE = 6;
const int LED = 7;

static const TempUnit SCALE=CELSIUS;

IRTemp ir(PIN_AQUIRE, PIN_CLOCK, PIN_DATA);

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}

void loop() {
  digitalWrite(LED, HIGH);
  float irtemp = ir.getIRTemperature(SCALE);
  float ambtemp = ir.getAmbientTemperature(SCALE);

  // IR:AMB format
  Serial.println(String(irtemp) + ":" + String(ambtemp));
  digitalWrite(LED, LOW);

  delay(1000);
}
