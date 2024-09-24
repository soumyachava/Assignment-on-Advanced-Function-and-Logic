{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "57d1f011-6d57-48fc-bf5f-e7b80704e13b",
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
    "#recursive_inner_plus.py\n",
    "def recursive_inner_plus_list(input_list):\n",
    "    for i in input_list:\n",
    "        if isinstance(i, list):\n",
    "            return find_innermost_list_recursive(i)\n",
    "    return [x + 1 for x in input_list]\n",
    "\n",
    "# Usage\n",
    "input_list = [10, 20, [30, [40, 50]]]\n",
    "print(recursive_inner_plus_list(input_list))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad8dffca-318a-49c6-bdf2-a29e84c31675",
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
