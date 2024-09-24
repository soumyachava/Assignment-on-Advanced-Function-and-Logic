{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "78ab4c1f-491f-431d-aa04-2525e86e2e06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 30]\n"
     ]
    }
   ],
   "source": [
    "def function_filter_list(input_list, threshold):\n",
    "    \n",
    "    return [x for x in input_list if x <= threshold]\n",
    "\n",
    "# Usage\n",
    "input_list = [10, 20, 30, 40, 50, 60]\n",
    "threshold = 30\n",
    "print(function_filter_list(input_list, threshold))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f34ffbd-e218-4885-8488-12ea7e4481b2",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
