{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4eb18139-be44-4c62-873d-553edc05b015",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[41, 51]\n"
     ]
    }
   ],
   "source": [
    "#while_inner_plus.py\n",
    "def while_inner_plus_list(input_list):\n",
    "    current_list = input_list\n",
    "    \n",
    "    while any(isinstance(i, list) for i in current_list):\n",
    "        for i in current_list:\n",
    "            if isinstance(i, list):\n",
    "                current_list = i\n",
    "                break\n",
    "\n",
    "    return [x + 1 for x in current_list]\n",
    "\n",
    "# Usage\n",
    "input_list = [10, 20, [30, [40, 50]]]\n",
    "print(while_inner_plus_list(input_list))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d5f0c37-f4db-4e72-b5d0-51544561920c",
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
