import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import { CommonButton } from './index'

describe('CommonButton', () => {
  it('renders a button', () => {
    // eslint-disable-next-line @typescript-eslint/no-empty-function
    render(<CommonButton onClick={() => {}}>Button</CommonButton>)
    const button  = screen.getByRole('button', {
      name: 'Button'
    })
    expect(button).toBeInTheDocument()
  })
})