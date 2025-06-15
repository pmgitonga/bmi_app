{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8dfdb8f-cfb1-4d76-b556-1fe718549077",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'weight' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m BMI \u001b[38;5;241m=\u001b[39m weight (kg) \u001b[38;5;241m/\u001b[39m (height (m) \u001b[38;5;241m^\u001b[39m \u001b[38;5;241m2\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'weight' is not defined"
     ]
    }
   ],
   "source": [
    "BMI = weight (kg) / (height (m) ^ 2)\n",
    "\n",
    "#And the categories are:\n",
    "\n",
    "#BMI < 18.5 → Underweight\n",
    "\n",
    "#18.5 ≤ BMI < 24.9 → Normal\n",
    "\n",
    "#25 ≤ BMI < 29.9 → Overweight\n",
    "\n",
    "#BMI ≥ 30 → Obese"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8983f46-81d6-4f81-b2ce-fe0d7aa1053d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "from pydantic import BaseModel\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "class BodyData(BaseModel):\n",
    "    height_cm: float\n",
    "    weight_kg: float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "689cb7fa-6366-4d3d-9ba9-d20bffee16c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.post(\"/bmi\")\n",
    "def calculate_bmi(data: BodyData):\n",
    "    height_m = data.height_cm / 100\n",
    "    bmi = data.weight_kg / (height_m ** 2)\n",
    "\n",
    "    if bmi < 18.5:\n",
    "        category = \"Underweight\"\n",
    "    elif 18.5 <= bmi < 24.9:\n",
    "        category = \"Normal weight\"\n",
    "    elif 25 <= bmi < 29.9:\n",
    "        category = \"Overweight\"\n",
    "    else:\n",
    "        category = \"Obese\"\n",
    "\n",
    "    return {\n",
    "        \"bmi\": round(bmi, 2),\n",
    "        \"category\": category\n",
    "    }"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
