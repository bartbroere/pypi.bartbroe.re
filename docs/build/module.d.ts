/**
 *
 * @param {undefined | function(): string} stdin
 * @param {undefined | function(string)} stdout
 * @param {undefined | function(string)} stderr
 */
export function setStandardStreams(stdin: undefined | (() => string), stdout: undefined | ((arg0: string) => any), stderr: undefined | ((arg0: string) => any)): void;
export type Module = any;
/**
 * @typedef {import('emscripten').Module} Module
 */
/**
 * The Emscripten Module.
 *
 * @private
 * @type {Module}
 */
export let Module: any;
