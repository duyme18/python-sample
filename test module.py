{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "07f589d8",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'my_module' has no attribute 'greet'",
     "output_type": "error",
     "traceback": [
      "\u001B[0;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[0;31mAttributeError\u001B[0m                            Traceback (most recent call last)",
      "Input \u001B[0;32mIn [15]\u001B[0m, in \u001B[0;36m<module>\u001B[0;34m\u001B[0m\n\u001B[1;32m      1\u001B[0m \u001B[38;5;28;01mimport\u001B[39;00m \u001B[38;5;21;01mmy_module\u001B[39;00m\n\u001B[0;32m----> 3\u001B[0m \u001B[38;5;28mprint\u001B[39m(\u001B[43mmy_module\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mgreet\u001B[49m\u001B[38;5;241m.\u001B[39m\u001B[38;5;18m__doc__\u001B[39m)\n",
      "\u001B[0;31mAttributeError\u001B[0m: module 'my_module' has no attribute 'greet'"
     ]
    }
   ],
   "source": [
    "import my_module\n",
    "\n",
    "print(my_module.greet.__doc__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65c472b6",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}