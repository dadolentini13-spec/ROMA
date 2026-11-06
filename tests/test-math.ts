import { add } from '../src/math.js';

if (add(2, 2) !== 4) {
  throw new Error('TypeScript runtime test failed');
}
console.log('TypeScript compilation and runtime test passed');
