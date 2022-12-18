import { MutableRefObject, useEffect, useRef } from 'react'

export const useOutsideClick = (
  callback: () => void
): MutableRefObject<HTMLDivElement | null> => {
  const ref = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    const handleClick = (event: Event): void => {
      const currentRef = ref.current

      if (currentRef && !currentRef?.contains(event.target as Node)) {
        callback()
      }
    }

    document.addEventListener('click', handleClick, true)

    return () => {
      document.removeEventListener('click', handleClick, true)
    }
  }, [callback, ref])

  return ref
}