import styled from '@emotion/styled'

export const StyledSvg = styled.svg`
  position: relative;
  display: inline-block;
  flex-shrink: 0;
  
  &.reverse {
    transform: rotate(180deg);
  }
`